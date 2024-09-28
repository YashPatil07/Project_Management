** Django REST API for User, Client, and Project Management **

OVERVIEW:
  This project is a Django-based REST API system designed for managing users, clients, and projects.
  
  The system consists of three primary entities:
  1. User: Registered users who are part of the system.
  2. Client: Clients that the system interacts with.
  3. Project: Projects associated with clients and assigned to multiple users.
     
  This API allows you to:
  1. Register new clients.
  2. Fetch information about clients.
  3. Edit or delete client details.
  4. Add new projects for clients and assign users to them.
  5. Retrieve assigned projects for logged-in users.

FEATURES:
1. Client Management

  1. Register a new client.
  2. Retrieve all clients or a specific client.
  3. Update client information.
  4. Delete client information.
  
2. Project Management

  1. Add new projects for a client.
  2. Assign multiple users to a project.
  3. Retrieve projects assigned to the logged-in user.

API ENDPOINTS:

1.Client Endpoints
  1. POST /api/clients/ - Register a new client.
  2. GET /api/clients/ - Fetch the list of all clients.
  3. GET /api/clients/{client_id}/ - Retrieve a specific client's information.
  4. PUT /api/clients/{client_id}/ - Update a specific client's information.
  5. DELETE /api/clients/{client_id}/ - Delete a client.

2.Project Endpoints
  1. POST /api/projects/ - Create a new project and assign users to the project.
  2. GET /api/projects/{project_id}/ - Retrieve details of a specific project.
  3. GET /api/projects/user/ - Retrieve the list of projects assigned to the logged-in user.


  
