--patients
INSERT INTO patients
(patient_name, age, gender, city)
VALUES
('Sneha',22,'Female','Hyderabad'),
('Rahul',30,'Male','Mumbai'),
('Priya',27,'Female','Chennai'),
('Arjun',35,'Male','Bangalore'),
('Kiran',25,'Male','Pune');
--doctors
INSERT INTO doctors
(doctor_name, specialization)
VALUES
('Dr. Sharma','Cardiology'),
('Dr. Reddy','Neurology'),
('Dr. Mehta','Orthopedics');
--appointments
INSERT INTO appointments
(patient_id, doctor_id, appointment_date)
VALUES
(1,1,'2026-06-10'),
(2,2,'2026-06-11'),
(3,1,'2026-06-12'),
(4,3,'2026-06-13'),
(1,1,'2026-06-14');
--bills
INSERT INTO bills
(appointment_id, amount)
VALUES
(1,1500),
(2,2000),
(3,1800),
(4,2500),
(5,1700);