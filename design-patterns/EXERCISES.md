1. Weather Report Generating System
Description:
Create a system that generates personalized weather reports
for different cities using the public weather API (e.g.
OpenWeatherMap). The system should allow the user to
selecting the report format (e.g. text, HTML, JSON).
Requirements:
• Report Factory: Use the factory pattern for authoring
different types of reports.
• Weather API Integration: Use the free one
API for downloading weather data.
• Flexibility: The code should be easy to extend
new report formats.
• User Interaction: Enablement
user to select the city and report format.
Libraries/API:
• Requests (for communicating with the weather API).
• JSON (for handling data and generating reports in the
JSON).
• HTML (optional, for generating reports in
HTML).

2. Connection Management System with Various APIs
Description:
Design a system that allows you to connect and interact with
various APIs (e.g. Twitter API, GitHub API). The system should
allow you to easily add new API integrations without
the need to modify the existing code.
Requirements:
• API Connection Factory: Implement the factory pattern
to create connections to various APIs.
• Modularity: Each API should be supported
via a separate module.
• Configurability: The system should allow for easy
configuration of access to various APIs (API keys, tokens
access).
• Simple User Interaction: Enable
the user to choose the API and basic operations for
execution.
Libraries/API:
• Requests (for communication with external APIs).
• OAuth (for authentication on demanding websites
authorization, e.g. Twitter, GitHub).
• JSON (for handling data from the API).

3. Database Connection Manager
Description:
Design a database connection manager that ensures that
there is only one connection instance in the entire application.
Use it in a simple data management system.
Requirements:
• Singleton Connections: Create a Singleton class that
manages the connection to the database.
• Database Operations: Implement basic ones
CRUD operations (Create, Read, Update, Delete).
• Security and Performance: Ensure safe and
efficient connection to the database.
• Testing: Allows you to test the connection to the database
data by performing several operations.
Libraries/API:
• SQLAlchemy or PyMySQL (to manage connection to
MySQL or other database).
• SQLite (as an alternative to local testing without
remote database needs).

4. Configuration Management System
Description:
Create a configuration management system that uses the pattern
Singleton to provide a single global configuration available in
different parts of the application.
Requirements:
• Singleton Configuration: Implement the Singleton class
storing the configuration.
• Load/Update Configuration: Ability to load i
updating configuration settings (e.g. from file, variables
environmental).
• Security: Ensure configuration is in place
safely stored and accessible.
• Use in Sample Application: Demonstration of use
configuration system in the sample application.
Libraries/API:
• JSON or YAML (for loading configuration from files).
• os and sys in Python (for handling environment variables and
command line arguments).

5. Document Template Management System
Description:
Create a system for managing document templates that
allows you to create, edit and clone existing templates.
Templates can be of different types such as formal letters,
reports, presentations.
Requirements:
• Template Prototypes: Implement prototypes for
different types of document templates.
• Clone Templates: Enable cloning
existing templates with possible modifications.
• Flexibility and Extensibility: The system should be
easy to expand with new types of templates.
• User Interface: Simple interface to choose from,
cloning and modifying templates.
Libraries/API:
• Tkinter or other GUI framework (for user interface).
• JSON/XML (for storing templates and their structure).

6. System for Creating Configuration for Multiple Environments
Description:
Design a system that allows you to create and manage
configurations for various environments (e.g. development, testing,
production), using the prototype pattern.
Requirements:
• Configuration Prototypes: Create prototype objects
configurations for different environments.
• Cloning and Customizing Configuration:
Allowing you to clone configurations from one environment to another
another with the possibility of modification.
• Maintain Consistency: Ensure that changes in
prototypes do not affect existing clones.
• Usage Demonstration: Example use of the system for
various configuration scenarios.
Libraries/API:
• YAML/JSON (for storage and manipulation
configurations).
• copy in Python (for deep cloning of objects).

7. Adapter For Various Payment Systems
Description:
Create a system that supports various payment systems (e.g. PayPal,
Stripe, credit cards) that have different APIs. System
should provide a uniform interface for payment processing
regardless of the selected supplier.
Requirements:
• Adaptation of Payment Interfaces: Create adapters for
each payment system to adapt them to a uniform one
interface.
• Flexibility and Extensibility: The system should be
easy to expand with new payment methods.
• Secure Transactions: Ensure your security
transactions and user data.
• Action Demonstration: Sample application
showing the use of adapters for various payment systems.
Libraries/API:
• SDK libraries of individual payment systems (e.g.
PayPal SDK, Stripe SDK).
• requests in Python (for possible HTTP connections).

8. Adapter For Different Types of Databases
Description:
Design a system that allows interaction with different databases
data (e.g. MySQL, PostgreSQL, SQLite) using unified
interface. The system should allow execution
basic database operations such as reading and writing
data.
Requirements:
• Adapting Database Interfaces: Create adapters
for various database systems.
• Uniform Operations Interface: Provide a consistent interface
to perform operations on data.
• Modularity and Scalability: Easy to add
support for new databases.
• Sample Use: Demonstration of use
system with various databases in practice
scenario.
Libraries/API:
• ORMs such as SQLAlchemy (for interacting with various databases
data).
• Drivers for individual databases (e.g. PyMySQL,
psycopg2).

9. Login Decorator For Functions
Description:
Create a system of decorators that can be applied to various
functions to log various aspects of their operation (e.g. time
execution, arguments, return values).
Requirements:
• Login Decorators: Implement decorators that
they log execution time, arguments and return values
functions.
• Flexibility: Decorators should be versatile and
Easy to apply to various functions.
• Configurable: Level configurable
login.
• Usage Demonstration: Example use
decorators in various functions.
Libraries/API:
• logging in Python (to handle logging).
• time (to measure execution time).

10. Decorator Enhancing Features with Additional Functionality
Description:
Design a system of decorators that add extra
functionality to functions, e.g. checking permissions,
caching results, error handling.
Requirements:
• Functional Decorators: Create decorators that
they add functionalities such as caching and checking
permissions, error handling.
• Versatility: Decorators should be applicable to
different types of functions.
• Ease of Use: Allowing easy application and
configuring decorators.
• Sample Implementations: Demonstration
practical use of decorators in various scenarios.
Libraries/API:
• functools in Python (for creating decorators
preserving function metadata).
• cachetools (for implementing caching).

11. Simplified Cloud Service Management Interface
Description:
Create a system with a facade that simplifies the use of various
cloud services (e.g. AWS, Azure, Google Cloud), enabling
basic operations such as instance management,
storing and reading data.
Requirements:
• Cloud Services Facade: Implement a facade that
offers a simplified interface to use various services
cloud computing.
• Modularity: Makes it easy to add support for
new cloud services.
• Sample Usage Scenarios: Demonstration of use
facades in typical cloud management scenarios.
• Flexibility: The system should be flexible and easy
to expand.
Libraries/API:
• SDK libraries of individual cloud service providers.
• requests in Python (for possible HTTP connections).

12. Facade for Managing Complex Login Systems
Description:
Design a system with a facade that simplifies the login process
various application modules (e.g. logging into files, databases,
external services), providing a uniform login interface.
Requirements:
• Login System Facade: Create a facade that
offers a consistent interface to various login systems.
• Configurable: Allowing for easy configuration and
switching between different login methods.
• Flexibility and Extensibility: The system should be
easy to expand with new login methods.
• Action Demonstration: Example of using the system in
different parts of the application.
Libraries/API:
• logging in Python (to handle logging).
• Libraries for interacting with databases (e.g. SQLAlchemy).
• Libraries for communicating with external logging services.

13. Proxy for Resource Access Control
Description:
Create a system using the Proxy pattern that controls access to
specific resources in the application, e.g. important documents or
confidential data. Proxy should require authentication before
granting access.
Requirements:
• Access Control Proxy: Implement a proxy that
requires authentication before providing access to the resource.
• Security: Ensure access to the resource
safe and controlled.
• Modularity: Can be easily expanded by
additional resources and authentication methods.
• Usage Demonstration: Example of proxy usage in
access control scenarios.
Libraries/API:
• getpass in Python (for secure password entry).
• hashlib (for secure storage and verification
passwords).

14. Caching Proxies for Network Services
Description:
Design a system using the Proxy pattern that is used for
caching responses from web services (e.g. weather API,
data services). The goal is to increase efficiency through
limiting the number of requests to the service.
Requirements:
• Caching Proxies: Implement a proxy that caches
responses from the web service.
• Performance Optimization: Reduce load
network and latency through caching.
• Cache Configurability: Allows configuration
cache lifetime and refresh rules.
• Usage Demonstration: Caching usage example
proxy with the selected API.
Libraries/API:
• requests in Python (for communicating with the API).
• cachetools or similar (for cache management).

15. Sorting System with Different Strategies
Description:
Create a system that allows you to sort data using
various sorting algorithms. The user should be able to
choose which sorting algorithm to use (e.g. sort
bubble, insert, quick sort).
Requirements:
• Strategy Pattern for Sorting Algorithms:
Implement different sorting algorithms separately
strategies.
• Flexibility in Algorithm Selection: Enable
user to choose the sorting algorithm.
• Modularity: Easy to add new algorithms
sorting to the system.
• Usage Demonstration: Example use
system in various sorting scenarios.
Libraries/API:
• Standard Python libraries.

16. Routing System with Various Strategies
Description:
Design a navigation system that allows for routing
routes using different strategies (fastest route, shortest
route, route avoiding traffic jams).
Requirements:
• Various Routing Strategies: Implement
different routing strategies as separate classes.
• Configurability of Strategy Selection: Enable
user to choose their preferred determination strategy
routes.
• Maps Integration: Use of map data
to demonstrate different strategies.
• Flexibility and Extensibility: Easy to add
new routing strategies.
Libraries/API:
• Map APIs, e.g. Google Maps API or OpenStreetMap.
• requests for queries to the map API (if required).

17. State Change Notification System
Description:
Create a system that enables various application components
subscribing to notifications about specific status changes
objects (e.g. change of order status, data update
user).
Requirements:
• Observer Pattern Implementation: Create
a mechanism that allows objects to subscribe to i
receive notifications about changes in the status of others
objects.
• Flexibility and Modularity: The system should
allow you to easily add new types of notifications and
subscribers.
• Usage Demonstration: An example where various
components respond to state changes.
• Security and Scalability: Ensuring that
the system works efficiently even with large numbers
subscribers.
Libraries/API:
• Standard Python libraries.

18. User Event Tracker
Description:
Design a system that tracks and responds to various events
user in the application (e.g. clicks, page scrolling, changes in
forms).
Requirements:
• User Event Observation System:
Implement a mechanism to track user events i
notifying subscribers about them.
• Event Response: Ability to respond to
events differently by different application components.
• Configurable and Extensible: Ease of use
configuring tracked events and adding new reactions.
• Sample Implementations: Demonstration of operation
system in practical scenarios.
Libraries/API:
• Libraries for handling UI events if the application has an interface
graphical (e.g. PyQt, Tkinter).
• Standard Python libraries for backend logic.

19. Product Collection Iterator
Description:
Create a system that allows you to iterate through
product collection in the online store. The collection should
allow for both forward and backward iteration.
Requirements:
• Implementing the Iterator Pattern: Create an iterator for
product collection that allows for iteration in both directions.
• Flexibility of Collections: The system should enable
easy to add new products to your collection.
• Usage Demonstration: Show how the iterator can be used
to view products in various scenarios.
• Support for Different Collection Types: Allowing easy
changes in the product storage structure without affecting
iteration logic.
Libraries/API:
• Standard Python libraries.

20. Iterator for Multidimensional Data Structures
Description:
Design a system that allows for iterative traversal
multidimensional data structures such as matrices or
tensor data structures, in various directions and dimensions.
Requirements:
• Multidimensional Iterator: Implement an iterator that
enables traversal of multidimensional structures
data.
• Iteration Configurability: Configurable
direction and dimension of iteration.
• Usage Demonstration: Example of using iterator in
operations on multidimensional data structures.
• Flexibility and Extensibility: Easy to adapt
iterator to different types of data structures.
Libraries/API:
• numpy or similar libraries to handle operations on
matrices or tensors.
