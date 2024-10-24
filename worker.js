// Allowed UUID for authentication
// generate a uuid with uuidgenerator.net
const AUTHORIZED_UUID = 'a68a03e4-534b-47a0-ac50-fbe0e64399fa';

// worker.js
addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request));
});

async function handleRequest(request) {

  const { method, url, headers } = request;
  const urlObj = new URL(url);

  const requestUuid = headers.get('X-Auth-UUID');

  if (!requestUuid || requestUuid !== AUTHORIZED_UUID) {
    return new Response('Unauthorized: Invalid or missing UUID', { status: 401 });
  }

  switch (method) {
    case 'GET':
      return await getTodos();

    case 'POST':
      const newTodo = await request.json();
      return await addTodo(newTodo);

    case 'DELETE':
      const todoId = urlObj.searchParams.get('id');
      return await deleteTodo(todoId);

    default:
      return new Response('Method Not Allowed', { status: 405 });
  }
}

async function getTodos() {
  // @ts-ignore
  const keys = await TODO_KV.list(); 
  const todos = await Promise.all(
    keys.keys.map(async key => {
      // @ts-ignore
      const todo = await TODO_KV.get(key.name, 'json');
      return { id: key.name, ...todo };
    })
  );
  return new Response(JSON.stringify(todos), {
    headers: { 'Content-Type': 'application/json' },
  });
}

async function addTodo(newTodo) {
  const id = crypto.randomUUID();
  // @ts-ignore
  await TODO_KV.put(id, JSON.stringify(newTodo));
  return new Response(JSON.stringify({ message: 'Todo added successfully', id }), {
    headers: { 'Content-Type': 'application/json' },
    status: 201
  });
}

async function deleteTodo(id) {
  if (!id) {
    return new Response('Bad Request: Missing ID', { status: 400 });
  }
  // @ts-ignore
  await TODO_KV.delete(id);
  return new Response('Todo deleted successfully', { status: 200 });
}
