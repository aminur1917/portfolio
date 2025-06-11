# Start with a JDK base image
FROM openjdk:17-jdk-slim

# Create app directory
WORKDIR /app

# Copy JAR into container
COPY target/webapp-0.0.1-SNAPSHOT.jar app.jar

# Run the app
ENTRYPOINT ["java", "-jar", "app.jar"]
