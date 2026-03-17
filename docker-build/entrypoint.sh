
echo "Starting"

flask db upgrade

echo "OK"

exec "$@"