# Log-Analysis

## Project Overview
>This is a SQL reporting tool developed in Python. It contains the data from news articles webiste. This application queires against the database and presents the results for questions like top articles,top authors and the down time of the server

### How to Run?

#### PreRequisites:
  * [Python3](https://www.python.org/)
  * [Vagrant](https://www.vagrantup.com/)
  * [VirtualBox](https://www.virtualbox.org/)

#### Setup Project:
  1. Install Vagrant and VirtualBox
  2. Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
  3. Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from here.
  4. Unzip this file after downloading it. The file inside is called newsdata.sql.
  5. Copy the content of this current repository, by either downloading or cloning it from
  [Here](https://github.com/chkrishnadheeraj/Log-Analysis-Reporting)
  
#### Launching the Virtual Machine:
  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command and Log in using the following command:
  
  ```
    $ vagrant up && vagrant ssh
  
  ```
  2. Change directory to /vagrant and look around with ls.

  ```
    $ cd /vagrant

  ```
  
#### Setting up the database and Creating Views:

  1. Load the data in local database using the command:
  
  ```
    psql -d news -f newsdata.sql
  ```
  The database includes three tables:
  * Authors
  * Articles
  * Log
  
  2. Use `psql -d news` to connect to database.
  
  3. Create view article_views using:
  ```
  create view article_views as select substring(path from 10) from log;
  ```
    
  4. Create view error_log_view using:
  ```
  create view error_view as select date(time),round(100.0*sum(case log.status when '200 OK' then 0 else 1 end)/count(log.status),2) 
  as "Error Percentage" from log group by date(time) 
  order by "Error Percentage" desc;
  ```
 
  
#### Running the queries:
  1. From the vagrant directory inside the virtual machine,run loganalysis.py using:
  ```
    $ python3 loganalysis.py
  ```
