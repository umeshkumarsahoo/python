

```
# Study Hours Tracker using Pixela API

This Python script allows you to track your study hours by interacting with the [Pixela API](https://pixe.la/). It helps you create a user, set up a graph to monitor your study hours, and log your study hours each day.

## Prerequisites

Make sure you have the following Python packages installed:

- `requests`
- `datetime`

You can install the `requests` library using pip:

```bash
pip install requests
```

## How the Script Works

### 1. User Creation

The script first creates a new Pixela user using the following endpoint:

```python
pixel_endpoint = "https://pixe.la/v1/users"
```

You will need to provide a `token`, `username`, and agree to the terms of service by setting the following parameters:

```python
user_params = {
    "token": token,
    "username": "umesh69",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
```

### 2. Graph Creation

Once the user is created, the script sets up a graph to track your study hours. The graph is created using the following endpoint:

```python
graph_endpoint = f"{pixel_endpoint}/{user_name}/graphs"
```

The parameters for creating the graph include:

- `id`: A unique identifier for the graph (e.g., "graph2").
- `name`: The name of the graph (e.g., "study python").
- `unit`: The unit of measurement (e.g., "hours").
- `type`: The type of data (e.g., "float").
- `color`: The color of the graph (e.g., "momiji").

### 3. Posting Study Hours

To log your study hours, the script uses the following endpoint:

```python
pixel_creation_endpoint = f"{pixel_endpoint}/{user_name}/graphs/graph2"
```

You can input the number of hours you studied for the day, and the script will post this data to Pixela.

```python
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("how many hours you studied: ")
}
```

### 4. Updating Study Hours (Optional)

If you need to update the number of hours you studied, you can use the following endpoint:

```python
pixel_put_endpoint = f"{pixel_endpoint}/{user_name}/graphs/graph2/{today.strftime('%Y%m%d')}"
```

This allows you to modify the logged hours.

```python
new_pixel = {
    "quantity": "2.5"
}
```

### 5. Deleting Data (Optional)

If you need to delete a specific day's data, you can use the following endpoint:

```python
delete_endpoint = f"{pixel_endpoint}/{user_name}/graphs/graph2/{today.strftime('%Y%m%d')}"
```

This will remove the entry for that day.

## Conclusion

This script provides an easy way to track your study hours using the Pixela API. You can extend it to track other habits or activities as well by modifying the graph parameters.
```
