from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, when, to_date, to_timestamp, initcap, explode, split, lower, trim, regexp_replace

def load_data(engine):
    
    ### Create a Spark session
    spark = SparkSession.builder.appName("SquirrelCensus").getOrCreate()

    park_data = spark.read.csv("./data/park-data.csv", header=True, inferSchema=True)
    squirrel_data = spark.read.csv("./data/squirrel-data.csv", header=True, inferSchema=True)



    #### Clean squirrel data
    squirrel_data = squirrel_data.dropDuplicates(['squirrel id'])
    squirrel_data =  squirrel_data.withColumnRenamed('Squirrel Latitude (DD.DDDDDD)', 'squirrel_latitude')
    squirrel_data =  squirrel_data.withColumnRenamed('Squirrel Longitude (-DD.DDDDDD)', 'squirrel_longitude')
    squirrel_data =  squirrel_data.withColumnRenamed('Above Ground (Height in Feet)', 'above_ground_height_feet')
    squirrel_data = squirrel_data.select([col(c).alias(c.lower().replace(' ', '_')) for c in squirrel_data.columns])
    squirrel_data = squirrel_data.fillna({'primary_fur_color': "none"})
    squirrel_data = squirrel_data.withColumn(
        'above_ground_height_feet',
        when(col('above_ground_height_feet').isNull(), lit(0)).otherwise(col('above_ground_height_feet'))
    )



    ### Clean park data

    park_data = park_data.select([col(c).alias(c.lower().replace(' ', '_')) for c in park_data.columns])
    park_data = park_data.dropDuplicates(['park_id'])
    park_data = park_data.fillna({'litter': "None"})
    park_data = park_data.withColumn('date', to_date(col('date'), 'M/d/yy'))
    park_data = park_data.withColumn('date', to_date(col('date'), 'M/d/yy'))
    park_data = park_data.withColumn('start_time', to_timestamp(col('start_time'), 'h:m:s a'))
    park_data = park_data.withColumn('area_name', initcap(col('area_name')))
    park_data = park_data.withColumn('end_time', to_timestamp(col('end_time'), 'h:m:s a'))


    ### Create other_animal_sightings DataFrame to be able to count other animal sightings by park

    park_data = park_data.withColumn(
        'other_animal_sightings',
        regexp_replace(col('other_animal_sightings'), r'\([^)]*\)', '')
    )
    animals_df = park_data.withColumn(
        'animal',
        explode(
            split(
                lower(trim(col('other_animal_sightings'))), ','
            )
        )
    )
    animals_df = animals_df.select('animal', 'park_id')
    other_animal_sightings_data = animals_df.withColumn(
        'animal', trim(col('animal'))
    )

    ### Create activities DataFrame to be able to count activities by squirrel

    squirrel_data = squirrel_data.withColumn(
        'activities',
        regexp_replace(col('activities'), r'\([^)]*\)', '')
    )

    activities_df = squirrel_data.withColumn(
        'activity',
        explode(
            split(
                lower(trim(col('activities'))), ','
            )
        )
    )
    activities_df = activities_df.select('activity', 'squirrel_id')
    activities_df = activities_df.withColumn(
        'activity', trim(col('activity'))
    )

    # Convert to Pandas and load into database
    squirrel_pandas = squirrel_data.toPandas()
    park_pandas = park_data.toPandas()
    other_animal_sightings_pandas = other_animal_sightings_data.toPandas()
    activities_df_pandas = activities_df.toPandas()

    # Load data into database
    squirrel_pandas.to_sql('squirrel_data', con=engine, if_exists='replace', index=False)
    park_pandas.to_sql('park_data', con=engine, if_exists='replace', index=False)
    other_animal_sightings_pandas.to_sql('other_animal_sightings', con=engine, if_exists='replace', index=False)
    activities_df_pandas.to_sql('activities', con=engine, if_exists='replace', index=False)

    # Stop the Spark session
    spark.stop()
