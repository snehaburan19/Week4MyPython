
db.patients.insertOne({
    patient_id:1,
    name:"Sneha",
    age:22,
    city:"Hyderabad"
});

db.appointments.insertOne({
    appointment_id:1,
    patient_id:1,
    doctor:"Dr. Sharma",
    date:"2026-06-10"
}); 

db.patients.find();

db.patients.updateOne(
    {patient_id:1},
    {$set:{city:"Mumbai"}}
);

db.patients.deleteOne(
    {patient_id:1}
); 

db.patients.aggregate([
{
   $group:{
      _id:"$city",
      totalPatients:{$sum:1}
   }
}
]);