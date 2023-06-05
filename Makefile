
test-no-volume:
	docker-compose -f docker-compose.yaml -f docker-compose-no-volume.yaml up

test-internal-volume:
	docker-compose -f docker-compose.yaml -f docker-compose-internal-volume.yaml up

test-hosted-volume:
	rm -rf data
	docker-compose -f docker-compose.yaml -f docker-compose-hosted-volume.yaml up

test-rm:
	rm -rf data
	docker-compose -f docker-compose.yaml -f docker-compose-internal-volume.yaml rm
	docker volume rm pg_stress_postgres_data -f