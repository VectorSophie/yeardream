DESC AIR_ROUTE;
DESC AIRPLANE;

SELECT route_from, route_to, airplane_id FROM AIR_ROUTE LEFT OUTER JOIN AIRPLANE ON AIR_ROUTE.route_id = AIRPLANE.route_id WHERE route_from = 'Korea' ORDER BY airplane_id ASC;
