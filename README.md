
# Cloudflare Workers To-Do API with KV Storage

This project is a simple **To-Do list API** built with **Cloudflare Workers** and **KV Storage**.

It allows you to add, retrieve, and delete to-do items via HTTP requests.

The API also includes an authentication mechanism to restrict access to authorized users.

## Features
- **GET**: Retrieve all to-do items.
- **POST**: Add a new to-do item.
- **Edit**: Edit a to-do item by ID
- **DELETE**: Remove a to-do item by ID.
- **Authentication**: Only requests with the correct UUID can interact with the API.

## Setup

### Cloudflare Setup
To set up Cloudflare Workers and KV Storage, follow these steps:

#### a. Create a KV Namespace:
1. Go to your **Cloudflare Dashboard**.
2. Select your domain and navigate to the **Workers** section.
3. Under the **KV** tab, create a new namespace (e.g., `todo-kv`).
4. Bind the KV namespace to your Worker script.

#### b. Worker Configuration:
1. Create a Worker from the **Workers** section.
2. Bind the KV Namespace to your Worker using the `TODO_KV` binding in the settings.

#### c. Deploy the Worker:
1. Copy the contents of `worker.js` to your Worker script.
2. Deploy the Worker.

### 3. Configure Authentication
The API uses a UUID for authentication. In this project, the authorized UUID is `a68a03e4-534b-47a0-ac50-fbe0e64399fa`. You can change this value in `worker.js` under the `AUTHORIZED_UUID` variable.

```javascript
const AUTHORIZED_UUID = 'a68a03e4-534b-47a0-ac50-fbe0e64399fa';
```

## API Endpoints

### 1. **GET**: Fetch All To-Do Items
- URL: `GET /`
- Headers: 
  - `X-Auth-UUID`: `a68a03e4-534b-47a0-ac50-fbe0e64399fa`

```bash
curl -X GET "https://your-worker-url.workers.dev/" \
  -H "X-Auth-UUID: a68a03e4-534b-47a0-ac50-fbe0e64399fa"
```

Response:
```json
[
  {
    "id": "generated-todo-id-1",
    "task": "Finish writing the API"
  },
  {
    "id": "generated-todo-id-2",
    "task": "Deploy Worker"
  }
]
```

### 2. **POST**: Add a New To-Do Item
- URL: `POST /`
- Headers: 
  - `X-Auth-UUID`: `a68a03e4-534b-47a0-ac50-fbe0e64399fa`
  - `Content-Type`: `application/json`
- Body: JSON object containing the new task (e.g., `{"task": "Do something"}`)

```bash
curl -X POST "https://your-worker-url.workers.dev/" \
  -H "Content-Type: application/json" \
  -H "X-Auth-UUID: a68a03e4-534b-47a0-ac50-fbe0e64399fa" \
  -d '{"task": "Write documentation"}'
```

Response:
```json
{
  "message": "Todo added successfully",
  "id": "generated-todo-id"
}
```

### 3. **DELETE**: Remove a To-Do Item
- URL: `DELETE /?id=<todo-id>`
- Headers: 
  - `X-Auth-UUID`: `a68a03e4-534b-47a0-ac50-fbe0e64399fa`

```bash
curl -X DELETE "https://your-worker-url.workers.dev/?id=<todo-id>" \
  -H "X-Auth-UUID: a68a03e4-534b-47a0-ac50-fbe0e64399fa"
```

Response:
```text
Todo deleted successfully
```

## Authentication
Only requests with the correct UUID can interact with the API. The UUID must be passed in the `X-Auth-UUID` header with every request. If the UUID does not match, the API will return a `401 Unauthorized` error.

Example unauthorized response:
```json
{
  "error": "Unauthorized: Invalid or missing UUID"
}
```

To test, use this UUID for authentication:
```
a68a03e4-534b-47a0-ac50-fbe0e64399fa
```
