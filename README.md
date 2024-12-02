sudo docker network create social
sudo docker run -d -p 8000:8000 --network=social  --name=social-post socialimageapp1:v2
sudo docker run -d -p 8001:8001 --env USER_PROFILE_SERVICE_URL=http://app1:8000/users --name=social-fetch --network=social socailimageapp2:v2
