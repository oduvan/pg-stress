#!/bin/sh
set -e

psql --user my_user my_database < /init_db.sql