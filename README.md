# EasyLendPC 

EasyLendPC is an innovative web-based platform designed to connect individuals and professionals who need short-term access to a laptop with those willing to lend theirs. The platform bridges the gap between urgent laptop needs and individuals or businesses that can offer their laptops for rent. By prov iding a trusted environment, EasyLendPC helps users meet pressing deadlines, handle unforeseen contingencies, and fulfill professional or personal commitments requiring a functional laptop, all within a negotiable rental framework.

The platform’s primary objective is to resolve challenges such as missed deadlines due to the unavailability of a computer, urgent short-term laptop needs during travel, and the inability of personal laptops to meet specific demands. EasyLendPC simultaneously offers business-minded individuals and companies an additional revenue stream by allowing them to rent out their laptops, monetizing otherwise idle hardware.

## Table of Content

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Deployment](#deployment)
- [Using the API documentation](#using-the-api-documentation)
- [Contributing](#contributing)
- [License](#license)


## Features
### Institution Dashboard

Institutions can:
- Manage Departments: Create and delete departments.
- Manage Teachers: Create and delete teachers.
- Manage Learners: Create and delete learners.

### Teacher Dashboard
Teachers can:
- Manage resources: Create and delete resources.
- View Resources: View resources they have created.
- Specific Resource Riew: View detailed content of a resource.

### Learner Dashboard
- View Resources: Access all resources available in their department.
- Detailed Resource View: Click on a resource to view its detailed content.
- User authentication and authorization

### Authentication and Access Control
- Role-Based Access: Different dashboards and functionalities are accessible based on the user's role (Institution, Teacher, Learner).
- User Authentication: Secure login and logout functionalities.


## Technologies Used

- **Backend**: Django, SQLite
- **Frontend**: HTML5, CSS, Flask, Jinja2
- **Database**: MySQL (development), POSTGRESQL (production)
- **Server**: Gunicorn
- **Deployment**: The application was deployed on render.com. [Visit the live app](https://resourcehub-0szu.onrender.com/)


## Setup and Installation
### Prerequisites

- Python 3.6 or higher
- Virtualenv
- MySQL (for development)

### Installation

Follow these steps to run the application on your local machine.
1. Clone the repository:
    ```bash
    git clone https://github.com/Abdulquyum/EasyLendPC.git
    cd EasyLendPC
    ```

2. Run the setup script:
    ```bash
    ./setup/setup_easylendpc.sh
    ```
   This script:
	- installs the python venv package on your system if it doesn't exist,
	- creates a virtual environment named *easylendpc_env*,
	- activates the virtual environment and installs the app dependencies (defined in setup/requirements.txt) in it, and
	- closes the virtual environment.

3. Start the virtual environment:
    ```bash
    source easylendpc_env/bin/activate
    ```

4. Start the *API* on one terminal:
    ```bash
    python3 -m api.telegram_bot.bot
    ```
    The API is configured to run on port 5001 of your machine, so ensure nothing else is running on that port.

5. Start the *app* on another terminal:
    ```bash
    python3 manage.py runserver    ```
    The app is configured to run on port 8000 of your machine, so ensure nothing else is running on that port. You can modify this setting in the *app/app.py* file.

6. Run the application:
Open your browser and navigate to http://127.0.0.1:8000/ to start using the app.


## Deployment
The application is deployed on [Render](https://render.com/). You can access it [here](https://resourcehub-0szu.onrender.com/).


## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.


## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
