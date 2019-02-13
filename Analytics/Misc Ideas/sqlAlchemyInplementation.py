# # Using SQLALchemy for SQL Engine Queries (Postgres)
# from sqlalchemy import create_engine
# import psycopg2
# import postgres_permissions


# Initialize Local parameters to access Postgres 
# database, for security purposes.
username = postgres_permissions.username
databaseName = postgres_permissions.databaseName
localhost = postgres_permissions.localhost

engine = create_engine(f'postgresql+psycopg2://{username}:{localhost}/{databaseName}')

# Instiatiate table in database.
# If the table update process fails,
# it already exists.

# try:
#     orderProductsPriorData.to_sql('order_products_prior', con=engine,if_exists='fail')
#     ordersData.to_sql('orders', con=engine,if_exists='fail')
#     aislesData.to_sql('aisles', con=engine,if_exists='fail' )
#     departmentsData.to_sql('departments', con=engine,if_exists='fail')
#     productsData.to_sql('products', con=engine,if_exists='fail')
# except:
#     pass


''' Read SQL Query function
    
    Parameter: query_string
    Description: For a given query string, instantiate a pandas DataFrame
    from a given connection
'''
def read_sql_query(query_string):
    return (pd.read_sql(query_string, con=engine))



read_sql_query('''
        SELECT 
            CASE 
                WHEN order_dow=0
                THEN 'Sunday'
                WHEN order_dow=1
                THEN 'Monday'
                WHEN order_dow=2
                THEN 'Tuesday'
                WHEN order_dow=3
                THEN 'Wednesday'
                WHEN order_dow=4
                THEN 'Thursday'
                WHEN order_dow=5
                THEN 'Friday'
                ELSE 'Saturday'
            END AS
                order_dow_string,
            COUNT(user_id) total_users
        FROM orders
        GROUP BY order_dow
    ''')