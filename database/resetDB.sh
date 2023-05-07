# check if the database exists
if [ -f flights.db ]; then
    echo "Database exists. Deleting..."
    rm -rf flights.db
fi
sqlite3 flights.db < schema.sql
sqlite3 flights.db < startingData.sql