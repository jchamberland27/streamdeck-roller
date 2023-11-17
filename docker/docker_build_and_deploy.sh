# utility script to build docker image
echo "Build and deploy streamdeck-roller docker image..."

# move dockerfile into place
cp dockerfile ../src/
cd ../src

# build and run docker image
docker image build -t streamdeck-roller .
docker run -d -p 5000:5000 streamdeck-roller

#cleanup
rm dockerfile

# dump out running containers
echo "Running containers after deployment:"
docker ps

echo "Done."