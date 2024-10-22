# EasyLendPC 

EasyLendPC is an innovative web-based platform designed to connect individuals and professionals who need short-term access to a laptop with those willing to lend theirs. The platform bridges the gap between urgent laptop needs and individuals or businesses that can offer their laptops for rent. By prov iding a trusted environment, EasyLendPC helps users meet pressing deadlines, handle unforeseen contingencies, and fulfill professional or personal commitments requiring a functional laptop, all within a negotiable rental framework.

The platform’s primary objective is to resolve challenges such as missed deadlines due to the unavailability of a computer, urgent short-term laptop needs during travel, and the inability of personal laptops to meet specific demands. EasyLendPC simultaneously offers business-minded individuals and companies an additional revenue stream by allowing them to rent out their laptops, monetizing otherwise idle hardware.

## Table of Content

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Using the API documentation](#using-the-api-documentation)
- [Contributing](#contributing)


## Features
EasyLendPC offers a range of features that provide users with a smooth and intuitive experience for lending and borrowing laptops. The platform is designed to cater to both individuals who want to lend out their PCs and those looking for a reliable short-term laptop solution. Here's a breakdown of the key features:

###  🖥️ Laptop Listing and Borrowing
Lend Out a Laptop: Users can list their laptops for lending, including essential details such as the laptop's name, description, and condition.
Admin Review: Every listing submitted by users is sent for admin approval before it’s displayed on the main site to ensure quality and accuracy.
Browse Available Laptops: Users can browse through the collection of available laptops and select one that fits their needs.
Price Negotiation via Telegram: Borrowers can negotiate prices and terms directly with the laptop owner through the integrated Telegram bot.

###  🔒 User Authentication
Signup/Login: Secure authentication using Django’s built-in authentication system.
Account Management: Once logged in, users can view and manage their account details, see the status of their listed laptops, and track borrowed items.
Admin Dashboard: Special access for admin users to manage and review laptop listings, user activity, and approvals.

###  📲 Telegram Integration
Telegram Bot: Users can communicate with the admin or laptop owners via a Telegram bot integrated into the platform.
Real-time Notifications: Receive instant updates about listing approvals, borrowing requests, and other important activities through the bot.

###  🌐 Responsive Design
Mobile-Friendly UI: Built with a responsive design using Bootstrap, EasyLendPC is fully accessible on any device, from desktops to smartphones, ensuring a seamless experience for users.
Dynamic Dashboard: Admin and user dashboards adapt to user roles, allowing for easy management of personal and administrative tasks.


## Technologies Used

- **Backend**: Django, SQLite
- **Frontend**: HTML5, CSS, Jinja2, Bootstrap
- **Database**: SQLite
- **Server**: Gunicorn

## Setup and Installation
### Prerequisites

- Python 3.6 or higher
- Virtualenv
- SQLite (for development)

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
    The API is configured to run on port 5000 of your machine, so ensure nothing else is running on that port.

5. Start the *app* on another terminal:
    ```bash
    python3 manage.py runserver    ```
    The app is configured to run on port 8000 of your machine, so ensure nothing else is running on that port. You can modify this setting in the *app/app.py* file.

6. Run the application:
Open your browser and navigate to http://127.0.0.1:8000/ to start using the app.


## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.



