
MIN_INTERVAL_QUERY = """SELECT
	MIN(intervalo) AS minInterval
FROM
	ecademprod.Proj_Monitoring"""


GET_DATA_QUERY = """SELECT 
	LAST_REC.idMonitoring,
	INFO.url,
	INFO.photoUrl,
	LAST_REC.Recent,
	HIST.`time`,
	HIST.statusCode
FROM
	(
	SELECT
			idMonitoring,
			MAX(lastUpdate) AS Recent
	FROM
			ecademprod.Proj_Monitoring_Hist
	GROUP BY
		idMonitoring
) AS LAST_REC
JOIN ecademprod.Proj_Monitoring_Hist AS HIST
ON
	LAST_REC.idMonitoring = HIST.idMonitoring
	AND LAST_REC.Recent = HIST.lastUpdate 
JOIN ecademprod.Proj_Monitoring AS INFO
ON INFO.id = LAST_REC.idMonitoring
ORDER BY 1 DESC"""