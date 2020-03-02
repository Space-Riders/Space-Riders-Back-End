# Space-Ryders Back End API Documentation

BaseURL : ``

<summary><b>POST - Register a new user</b></summary>

<b>Endpoint:</b> `/registration/`
</br>
Requires an object with a username, password1 and password2:

```json
{
  "username": "testuser123",
  "password1": "password123",
  "password2": "password123"
}
```

When successful will return status code of 201 (CREATED), and an object containing the key/token (example):

```json
{
  "key": "39ef2ef932da123b8f91955b813be06fa123ffd3"
}
```




<summary><b>POST - Login an existing user</b></summary>

<b>Endpoint:</b> `/login/`
</br>
Requires an object with a username, password:

```json
{
  "username": "testuser123",
  "password": "password123"
}
```

When successful will return status code of 200 (OK), and an object containing the key/token (example):

```json
{
  "key": "39ef2ef932da123b8f91955b813be06fa123ffd3"
}
```




<summary><b>GET - Get user's intial room</b></summary>

<b>Endpoint:</b> `/adv/init/`
</br>
Requires Authorization key in headers with token as the value.

When successful will return status code of 200 (OK), and an object containing the user and room details (example):

```json
{
  "uuid": "a303434f-e5cc-4a5a-9ad9-46d7ac24c75b",
  "name": "testuser",
  "title": "nebula-e87",
  "x_coor": 0,
  "y_coor": 42,
  "description": "Nebula Cluster",
  "nextRooms": [
    {
      "n": 1027
    },
    {
      "e": 1051
    },
    {
      "s": 1071
    },
    {
      "w": 0
    }
  ],
  "players": []
}
```



<summary><b>POST - Warp ryder to another solar system</b></summary>
<b>Endpoint:</b> `/adv/move/`
</br>
Requires Authorization key in headers with token as the value.
</br>
Requires a request object with the direction:

```json
{
  "direction": "n"
}
```

When successful will return status code of 200 (OK), and an object containing the user and room details (example):

```json
{
  "name": "admin",
  "title": "planet-w315",
  "description": "Perplexed by the ordinary twin stars, you trod along past the invisible, habitat.",
  "players": [],
  "nextRooms": [
    {
      "n": 1005
    },
    {
      "e": 1028
    },
    {
      "s": 1050
    },
    {
      "w": 0
    }
  ],
  "error_msg": ""
}
```


<summary><b>GET - Get all rooms</b></summary>
<b>Endpoint:</b> `/adv/matrix/`
</br>
No token, request body, or headers required.
</br>
Requires a response object with the direction:

```json
{
  "direction": "n"
}
```

When successful will return status code of 200 (OK), and an array of arrays containing 1s ## and 0s that signify which are rooms and which are not.

