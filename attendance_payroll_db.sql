1. Find Employees with Highest Attendance

SELECT
    employee_id,
    COUNT(*) AS attendance_count
FROM attendance
WHERE status = 'Present'
GROUP BY employee_id
ORDER BY attendance_count DESC;


2. Calculate Department-wise Salary Expense

SELECT
    e.department,
    SUM(p.calculated_salary) AS total_salary_expense
FROM payroll p
JOIN employees e
ON e.id = p.employee_id
GROUP BY e.department;


3. List Absent Employees for a Given Date

SELECT
    e.id,
    e.name,
    a.attendance_date
FROM employees e
JOIN attendance a
ON e.id = a.employee_id
WHERE a.status = 'Absent'
AND a.attendance_date = '2026-06-01';


4. Generate Monthly Payroll Report

SELECT
    e.id,
    e.name,
    p.payroll_month,
    p.present_days,
    p.calculated_salary
FROM payroll p
JOIN employees e
ON e.id = p.employee_id
ORDER BY p.payroll_month;


5. Rank Employees Based on Attendance Percentage

SELECT
    employee_id,
    ROUND(
        (SUM(CASE WHEN status = 'Present' THEN 1 ELSE 0 END) * 100.0)
        / COUNT(*),
        2
    ) AS attendance_percentage
FROM attendance
GROUP BY employee_id
ORDER BY attendance_percentage DESC;