SELECT jobs.JOB_TITLE, COUNT(employees.EMPLOYEE_ID) FROM employees INNER JOIN jobs ON employees.JOB_ID = jobs.JOB_ID GROUP BY jobs.JOB_TITLE;
SELECT departments.MANAGER_ID, MIN(employees.SALARY) FROM employees INNER JOIN departments ON employees.MANAGER_ID = departments.MANAGER_ID;
SELECT departments.DEPARTMENT_ID, departments.DEPARTMENT_NAME, SUM(employees.SALARY) FROM departments INNER JOIN employees ON departments.DEPARTMENT_ID = employees.DEPARTMENT_ID GROUP BY departments.DEPARTMENT_NAME;
SELECT jobs.JOB_ID, AVG(employees.SALARY) FROM employees INNER JOIN jobs ON jobs.JOB_ID = employees.JOB_ID WHERE jobs.JOB_TITLE != "Programmer" GROUP BY jobs.JOB_ID;
SELECT JOB_ID, MAX(SALARY) FROM employees GROUP BY JOB_ID HAVING MAX(SALARY) >= 4000;
SELECT AVG(SALARY) FROM employees GROUP BY DEPARTMENT_ID HAVING COUNT(EMPLOYEE_ID) > 10;