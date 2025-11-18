# Node.js
#
# docker run -itd \
#	--link mysql:mysql \
#	-p 3000:3000 \
#	-h jorrellsmith.com \
#	--name node-app \
#	sabatiel180/my-portfolio:v1
#

FROM python:3.12

Label maintainer="Jorrell Smith <jorrells@linux.com>"


# Set the working directory inside the container
WORKDIR /app

# Copy your Python application code into the container
COPY . /app

# Install any required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Define the command to run your application when the container starts
CMD ["python", "Main.py"]


#COPY /html /var/www/html
#RUN rm /var/www/html/index.html
#RUN a2enmod ssl && a2ensite default-ssl
#EXPOSE 3000
#CMD ["node", "app.js"]

#ENTRYPOINT service apache2 restart && bash 