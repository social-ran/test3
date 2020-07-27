# Base our app image off of the WALKOFF App SDK image
FROM frikky/shuffle:app_sdk as base

# We're going to stage away all of the bloat from the build tools so lets create a builder stage
FROM base as builder

# Install all alpine build tools needed for our pip installs
RUN apk --no-cache add --update alpine-sdk libffi libffi-dev musl-dev openssl-dev

# Install all of our pip packages in a single directory that we can copy to our base image later
RUN mkdir /install
WORKDIR /install
COPY requirements.txt /requirements.txt

RUN pip install --prefix="/install" -r /requirements.txt


# Switch back to our base image and copy in all of our built packages and source code
FROM base
COPY --from=builder /install /usr/local
COPY src /app

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple selenium
RUN yum -y install https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
RUN wget http://npm.taobao.org/mirrors/chromedriver/2.41/chromedriver_linux64.zip
RUN cp ./chromedriver_linux64.zip /usr/bin
RUN cd /usr/bin
RUN unzip chromedriver_linux64.zip
RUN chmod +x /usr/bin/chromedriver
# Install any binary dependencies needed in our final image
# RUN apk --no-cache add --update my_binary_dependency

# Finally, lets run our app!
WORKDIR /app
CMD python app.py --log-level DEBUG
