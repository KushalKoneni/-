# check if the database exists
if [ -f catalogueData.db ]; then
    echo "Database exists. Deleting..."
    rm -rf catalogueData.db
fi
sqlite3 catalogueData.db < schema.sql
sqlite3 catalogueData.db < catalogueData.sql