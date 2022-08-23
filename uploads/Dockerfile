
FROM --platform=linux/amd64 swaggerza/nestjs-tensorflow:v0.0.1
WORKDIR /usr/src/app
COPY . .
RUN npm install
CMD ["npm","start"]
EXPOSE 80 

# 1. สร้าง dockerfile
# 2. สร้าง image : docker build -t nitikornchumnankul/api-upload-regina:v0.0.1 .
# 3. ใช้ docker image โดยใช้คำสั่ง docker run -p 3000:80 -d nitikornchumnankul/api-upload-regina:v0.0.1 
# 4. เอา docker image ไปเก็บที่ Docker hub  โดยใช้คำสัง docker push nitikornchumnankul/api-upload-regina:v0.0.1 
# 5. ดึง docker image จาก Docker hub โดยใช้คำสั่ง docker pull nitikornchumnankul/api-upload-regina:v0.0.1 


# docker ps 
# docker ps -a
# คำสังลบ container
# docker rm d3007b49ec4b
# docker rmi image id
# docker rm $(docker ps -aq)
