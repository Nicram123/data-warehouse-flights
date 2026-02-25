from pyspark.sql.types import *

airlines_schema = StructType([
    StructField("IATA_CODE", StringType(), True),
    StructField("AIRLINE", StringType(), True)
])

airports_schema = StructType([
    StructField("IATA_CODE", StringType(), True),
    StructField("AIRPORT", StringType(), True),
    StructField("CITY", StringType(), True),
    StructField("STATE", StringType(), True),
    StructField("COUNTRY", StringType(), True),
    StructField("LATITUDE", DoubleType(), True),
    StructField("LONGITUDE", DoubleType(), True)
])

flights_schema = StructType([
    StructField("YEAR", IntegerType(), True),
    StructField("MONTH", IntegerType(), True),
    StructField("DAY", IntegerType(), True),
    StructField("DAY_OF_WEEK", IntegerType(), True),
    StructField("AIRLINE", StringType(), True),
    StructField("FLIGHT_NUMBER", IntegerType(), True),
    StructField("TAIL_NUMBER", StringType(), True),
    StructField("ORIGIN_AIRPORT", StringType(), True),
    StructField("DESTINATION_AIRPORT", StringType(), True),
    StructField("SCHEDULED_DEPARTURE", StringType(), True),
    StructField("DEPARTURE_TIME", StringType(), True),
    StructField("DEPARTURE_DELAY", IntegerType(), True),
    StructField("TAXI_OUT", IntegerType(), True),
    StructField("WHEELS_OFF", StringType(), True),
    StructField("SCHEDULED_TIME", IntegerType(), True),
    StructField("ELAPSED_TIME", IntegerType(), True),
    StructField("AIR_TIME", IntegerType(), True),
    StructField("DISTANCE", IntegerType(), True),
    StructField("WHEELS_ON", StringType(), True),
    StructField("TAXI_IN", IntegerType(), True),
    StructField("SCHEDULED_ARRIVAL", StringType(), True),
    StructField("ARRIVAL_TIME", StringType(), True),
    StructField("ARRIVAL_DELAY", IntegerType(), True),
    StructField("DIVERTED", IntegerType(), True),
    StructField("CANCELLED", IntegerType(), True),
    StructField("CANCELLATION_REASON", StringType(), True),
    StructField("AIR_SYSTEM_DELAY", IntegerType(), True),
    StructField("SECURITY_DELAY", IntegerType(), True),
    StructField("AIRLINE_DELAY", IntegerType(), True),
    StructField("LATE_AIRCRAFT_DELAY", IntegerType(), True),
    StructField("WEATHER_DELAY", IntegerType(), True)
])


silver_airlines_schema = StructType([
    StructField("airline_key", StringType(), True),       # IATA code
    StructField("airline_name", StringType(), True),
    StructField("valid_from", TimestampType(), True),
    StructField("valid_to", TimestampType(), True),
    StructField("is_current", BooleanType(), True),
    StructField("load_timestamp", TimestampType(), True)
])

silver_airports_schema = StructType([
    StructField("airport_key", StringType(), True),       # IATA code
    StructField("airport_name", StringType(), True),
    StructField("city", StringType(), True),
    StructField("state", StringType(), True),
    StructField("country", StringType(), True),
    StructField("latitude", DoubleType(), True),
    StructField("longitude", DoubleType(), True),
    StructField("valid_from", TimestampType(), True),
    StructField("valid_to", TimestampType(), True),
    StructField("is_current", BooleanType(), True),
    StructField("load_timestamp", TimestampType(), True)
])

silver_date_schema = StructType([
    StructField("date_key", DateType(), True),
    StructField("year", IntegerType(), True),
    StructField("month", IntegerType(), True),
    StructField("day", IntegerType(), True),
    StructField("day_of_week", IntegerType(), True),
    StructField("load_timestamp", TimestampType(), True)
])

silver_aircraft_schema = StructType([
    StructField("aircraft_key", IntegerType(), True),
    StructField("tail_number", StringType(), True),
    StructField("load_timestamp", TimestampType(), True)
])

silver_cancellation_schema = StructType([
    StructField("cancellation_reason_key", IntegerType(), True),
    StructField("code", StringType(), True),
    StructField("description", StringType(), True),
    StructField("load_timestamp", TimestampType(), True)
])

silver_route_schema = StructType([
    StructField("route_key", IntegerType(), True),
    StructField("origin_airport_key", StringType(), True),
    StructField("destination_airport_key", StringType(), True),
    StructField("load_timestamp", TimestampType(), True)
])

# FactFlights (docelowa tabela faktów)
gold_fact_flights_schema = StructType([
    StructField("flight_id", IntegerType(), True),
    StructField("date_key", DateType(), True),
    StructField("airline_key", StringType(), True),
    StructField("route_key", IntegerType(), True),
    StructField("aircraft_key", IntegerType(), True),
    StructField("cancellation_reason_key", IntegerType(), True),
    StructField("cancelled", IntegerType(), True),
    StructField("diverted", IntegerType(), True),
    StructField("scheduled_departure", StringType(), True),
    StructField("departure_time", StringType(), True),
    StructField("wheels_off", StringType(), True),
    StructField("wheels_on", StringType(), True),
    StructField("arrival_time", StringType(), True),
    StructField("scheduled_arrival", StringType(), True),
    StructField("taxi_out", IntegerType(), True),
    StructField("taxi_in", IntegerType(), True),
    StructField("distance", IntegerType(), True),
    StructField("time", IntegerType(), True),
    StructField("elapsed_time", IntegerType(), True),
    StructField("departure_delay", IntegerType(), True),
    StructField("arrival_delay", IntegerType(), True),
    StructField("air_system_delay", IntegerType(), True),
    StructField("security_delay", IntegerType(), True),
    StructField("airline_delay", IntegerType(), True),
    StructField("late_aircraft_delay", IntegerType(), True),
    StructField("weather_delay", IntegerType(), True),
    StructField("scheduled_time", IntegerType(), True),
    StructField("flight_number", StringType(), True),
    StructField("load_timestamp", TimestampType(), True)
])


