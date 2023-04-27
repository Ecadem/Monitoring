
SELECT_QUERY = """
SELECT 
    id, 
    url, 
    intervalo 
FROM ecademprod.Proj_Monitoring WHERE isActive = 1;"""


CREATION_QUERY = """INSERT INTO ecademprod.Proj_Monitoring_Hist
    (
        idMonitoring,
        lastUpdate,
        time,
        statusCode
    )
    VALUES
    (
        '{}',
        '{}',
        '{}',
        '{}'
    );"""