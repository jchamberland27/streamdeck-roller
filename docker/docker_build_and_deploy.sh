# utility script to build docker image
echo "Build and deploy streamdeck-roller docker image..."

#set $1 to default port if not passed in
if [ -z "$1" ]
  then
    echo "No port argument supplied, using default port 5000"
    set -- "5000"
fi

# move dockerfile into place
cp Dockerfile ../src/
cd ../src

# build and run docker image on port passed into script
docker image build -t streamdeck-roller .
docker run -d -p $1:5000 streamdeck-roller

#cleanup
rm Dockerfile

# dump out running containers
echo "Running containers after deployment:"
docker ps

echo "Done."