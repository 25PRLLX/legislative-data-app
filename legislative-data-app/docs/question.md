1. Discuss your strategy and decisions implementing the application. Please, consider time complexity, effort cost, technologies used, and any other variables you understand as important in your development process.

My strategy for this application was to build it in a way that efficiently handles large datasets while keeping scalability in mind. Here’s a breakdown of the key considerations:

Technologies Used: I chose Django as the web framework due to its built-in ORM for easy database management and its ability to work with structured data like the CSV files provided. This reduced the overall development effort as Django abstracts many complexities, such as database interactions and URL routing.

Time Complexity: Time complexity was kept low by ensuring bulk inserts of data rather than row-by-row processing. Additionally, using Django’s ORM allowed me to perform efficient database queries. For example, get_or_create() was used for data imports to minimize redundant database lookups.

Effort Cost: The decision to allow NULL sponsors for bills was to reduce the complexity of handling missing data. This decision decreased the effort spent on validation checks.

Modular Approach: The data import was divided into three key steps (legislators, bills, votes), allowing flexibility and clarity. This modularity ensures that new data structures can be integrated easily in the future.

Scalability: The solution can scale well because it leverages Django’s ORM and relational database, which is capable of handling future data growth. Optimizations like using foreign keys for relationships ensured that queries are efficient even as the dataset grows.


2. How would you change your solution to account for future columns that might be requested, such as “Bill Voted On Date” or “Co-Sponsors”?
To handle future changes like adding columns such as "Bill Voted On Date" or "Co-Sponsors", I would approach it as follows:

Database Schema Changes: New fields could be easily added to the Bill model, and I would run migrations to update the database schema accordingly. For example, vote_date and a many-to-many relation for co-sponsors can be added in the Bill model.

Flexible Import Process: I believe the import logic in import_data.py would need to handle new fields dynamically, ensuring that any future CSV formats are read and mapped to the appropriate model fields. This might require extending the data parsing logic to accommodate variable numbers of columns.

Backward Compatibility: I also believe that the current solution is modular enough to accommodate these changes without breaking the existing logic. Future columns can be treated as optional initially, which ensures backward compatibility with existing data.

3. How would you change your solution if instead of receiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for?
If the task was to generate CSVs from data rather than read them, I would:

Querying the Database: Use Django’s ORM to query the database and retrieve the necessary data for the report.

CSV Output: Utilize Python’s built-in csv module to generate CSV files. This would be achieved by querying the database and writing the resulting data to a file in the required CSV format. The Django management command could be extended to support export functionality.

Flexibility: I believe this approach would ensure that the export process is flexible, and any changes in data structure could be accommodated easily by adjusting the queries and fields to be exported.

4. How long did you spend working on the assignment?

I worked approximately 5 hours on the project. Although this is more than the recommended 2-3 hours, much of the time was spent refining the code. Initially, I opted to consume the data from the CSV and reflect it on the front end, using only views.py. I encountered a few small issues in making sure the data was consumed correctly, but everything worked out in the end. I pushed this first solution to Git.

I wasn’t very satisfied with consuming the data directly from the CSV without being able to manipulate it more comprehensively, so I decided to create models (models.py). This makes the code a bit more efficient, and it's easier to add data to the existing dataset if needed.

In the first block, I spent around 2 hours out of the total 5.

I didn’t create tests for the code since it’s an assessment, and I believe that adding tests would extend the "delivery time" by a few more hours.