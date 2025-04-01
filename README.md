# CS 665 Project 1
Repository for Project 1 for class CS665 - Intro to Database Systems at Wichita State University (Spring 2025)

## Proposal
- Project 1 will be about creating a small database application for a mock business or organization. For my project, I will be creating such an app for a mock airplane maintenance shop. This proposal will outline what such a mock shop would do and then explain how my project would benefit it (ie. the “story).
- Next, this proposal will explain the choice of database software along with a tentative database schema. Lastly, this proposal covers the choice of programming language and other aspects of the application that will be used.
- By applying SQLite database software to the use-case of an airplane maintenance shop, and then providing a GUI for the user to interact with the database, this project aims to explore how to make a reliable tool for tracking information that might be used to ensure that serviced aircraft remain safe and airworthy.

### User Story
- The mock business will be that of an airplane maintenance shop for general aviation (or “GA”) airplanes. This shop would provide routine maintenance and repairs for such GA airplanes. In general, it works like you might expect: an airplane owner brings in their airplane for service, the shop assigns a mechanic to do the work, and then the owner pays the shop. The critical part is in providing evidence of safe work.

- GA airplanes have specific maintenance requirements that must be met per FAA regulations. And that maintenance must be completed by certified mechanics using airworthy parts. Failure to provide evidence of meeting such requirements and certifications can result in punitive actions ranging from fines to license or certification forfeiture. It is therefore vitally important for any airplane maintenance shop to keep good records of the work done, the parts and labor used, and the airplane for which service was provided.

### Database Software
- For this project, the database software that will be used is SQLite. SQLite is the most popular open-source database software in the world. This means it is well-understood, mature, and has plenty of resources: all features that will contribute to the needed robustness of the data. Below is a tentative database schema for the project. It consists of 4 tables: Airplanes, Mechanics, Parts, and Services.

#### AIRPLANES Table Schema
| **Field Name** | **Data Type** | **Description**                                     |
| -------------- | ------------- | --------------------------------------------------- |
| tail_number    | TEXT          | FAA-registered tail number unique to each airplane. |
| make           | TEXT          | Manufacturer (eg. “Cessna”)                         |
| model          | TEXT          | Model (eg. “172”)                                   |
| year           | INTEGER       | Year of manufacture.                                |

#### MECHANICS Table Schema
| **Field Name**             | **Data Type** | **Description**                                                         |
| -------------------------- | ------------- | ----------------------------------------------------------------------- |
| mechanic_id                | INTEGER       | Primary Key unique for each mechanic.                                   |
| first_name                 | TEXT          | The mechanic's first name.                                              |
| last_name                  | TEXT          | The mechanic's last name.                                               |
| certification_last_renewed | DATE          | Date of last certification renewal. Mechanics must renew every 2 years. |

#### PARTS Table Schema
| **Field Name**          | **Data Type** | **Description**                                |
| ----------------------- | ------------- | ---------------------------------------------- |
| part_id                 | INTEGER       | Primary Key unique for each part.              |
| part_name               | TEXT          | Name of the part.                              |
| vendor_name             | TEXT          | Name of the supplier that provided the part.   |
| airworthiness_certified | DATE          | Date when the part was certified as airworthy. |

#### SERVICES Table Schema
| **Field Name**      | **Data Type** | **Description**                                                   |
| ------------------- | ------------- | ----------------------------------------------------------------- |
| service_id          | INTEGER       | Primary Key unique for each service.                              |
| service_description | TEXT          | A short text description of the service performed.                |
| service_date        | DATE          | Date that the work was performed.                                 |
| airplane_id         | INTEGER       | Foreign Key. Id of the airplane for which the work was performed. |
| part_id             | INTEGER       | Foreign Key. Id of the part used for the work.                    |
| mechanic_id         | INTEGER       | Foreign Key. Id of the mechanic who did the work.                 |

### Programming Language
For the programming language, the application will use python. Python is used for a similar reason as SQLite: it is well-understood and popular, and therefore well-supported. For the front-end, a GUI will be made using tkinter. Tkinter is chosen because it is a built-in python library, and so it does not require many dependencies that might introduce unnecessary complications.

### 