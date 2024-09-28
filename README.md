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

  A. Register a new client.
  B. Retrieve all clients or a specific client.
  C. Update client information.
  D. Delete client information.
  
2. Project Management

  A. Add new projects for a client.
  B. Assign multiple users to a project.
  C. Retrieve projects assigned to the logged-in user.

API ENDPOINTS:

1.Client Endpoints
  -> POST /api/clients/ - Register a new client.
  -> GET /api/clients/ - Fetch the list of all clients.
  -> GET /api/clients/{client_id}/ - Retrieve a specific client's information.
  -> PUT /api/clients/{client_id}/ - Update a specific client's information.
  -> DELETE /api/clients/{client_id}/ - Delete a client.

2.Project Endpoints
  -> POST /api/projects/ - Create a new project and assign users to the project.
  -> GET /api/projects/{project_id}/ - Retrieve details of a specific project.
  -> GET /api/projects/user/ - Retrieve the list of projects assigned to the logged-in user.


  
