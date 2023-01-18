const functions = require("firebase-functions");

const express = require("express");
const app = express();

const fs = require("fs");
const swig = require("swig");
//var QRCode = require("qrcode");
//var canvas = document.getElementById("canvas");


const admin = require("firebase-admin");
admin.initializeApp(functions.config().firebase);

app.get("/", function(req, res) {
  res.send("Hello World");
});

// app.get("/qr", function(req, res) {
//   res.send(`<html>
//   <input id="text" type="text" value="https://hogangnono.com" style="width:80%" /><br />
//   <div id="qrcode"></div>
//   <script>
//   var qrcode = new QRCode("qrcode");

// function makeCode () {		
// 	var elText = document.getElementById("text");
	
// 	if  (!elText.value) {
// 		alert("Input a text");
// 		elText.focus();
// 		return;
// 	}
	
// 	qrcode.makeCode("rif a");
// }

// makeCode();

// </script>
//   </html>`);

//   //   QRCode.toCanvas(canvas, "sample text", function (error) {
//   //   if  (error) console.error(error)
//   //   console.log("success!");
//   //   });
// });

// app.get("/try", function(req, res) {
//   //res.send("Hello World");
//   const email1 = "hjuidhsidhi";
//   const databaseEmail1 = admin.database().ref("users/" + email1);
//   res.send("done");
//   databaseEmail1.set(email1);
// });

// app.get("/contact", function(req, res) {
//   res.send("contact");
// });

// app.get("/swig", function(req, res) {
//   // var template1 = swig.compileFile("/view/home.html");
//   // var output = template1();
//   // res.writeHead(200, { "Content-Type": "text/html" });
//   // res.send(output);
// });

// app.get("/dashboard", function(req, resp) {
//   fs.readFile("../public/index.html", function(error, pgResp) {
//     if  (error) {
//       resp.writeHead(404);
//       resp.write("Contents you are looking are Not Found");
//     } else {
//       resp.writeHead(200, { "Content-Type": "text/html" });
//       resp.write(pgResp);
//     }

//     resp.end();
//   });
// });

// app.get("/update", function(req, res) {
//   var id = req.query.id;
//   var nama = req.query.nama;
//   var kota = req.query.kota;
//   const databaseNama = admin.database().ref("users").child(id).child("/nama");
//   const databaseKota = admin.database().ref("users").child(id).child("/kota");
//   res.send("done");
//   databaseNama.set(nama);
//   databaseKota.set(kota);

// });

// app.get("/posting", function(req, res) {
//   var id = req.query.id;
//   var suhu = req.query.suhu;
//   // var kota = req.query.kota;
//   const databaseNama = admin.database().ref("users").child(id).child("/suhu");
//   // const databaseKota = admin.database().ref("users").child("suhuku").child("suhu");
//   res.send("done");
//   databaseNama.set(suhu);
//   // databaseKota.set(kota);

// });

// app.get("/getsuhu", function(req, res) {
//   var id = req.query.id;
//   const params = req.url.split("/");
//   const eventId = params[2];
//   return admin.database().ref("users/suhuku").once("value", (snapshot) => {
//     var event = snapshot.val();
//     res.send(event.suhu);
//   });
// });

// app.get("/absen", function(req, res) {
//   var id = req.query.id;
//   var jurusan = req.query.jurusan;
//   // var kota = req.query.kota;
//   const databaseNama = admin.database().ref("absen").child(jurusan).child(id);
//   // const databaseKota = admin.database().ref("users").child(id).child("/kota");
//   res.send("done");
//   databaseNama.set("hadir");
//   // databaseKota.set(kota);

// });

// app.get("/deleteabsen", function(req, res) {
//   // var id = req.query.id;
//   // var jurusan = req.query.jurusan;
//   // var kota = req.query.kota;
//   const databaseNama = admin.database().ref("absen").child("TKR").child("data");
//   const databaseNama1 = admin.database().ref("absen").child("MM").child("data");
//   const databaseNama2 = admin.database().ref("absen").child("TKJ").child("data");
//   const databaseNam = admin.database().ref("absen").child("TKR");
//   const databaseNam1 = admin.database().ref("absen").child("MM");
//   const databaseNam2 = admin.database().ref("absen").child("TKJ");
//   //const databaseNama = admin.database().ref("absen").child("T").child("data");
//   // const databaseKota = admin.database().ref("users").child(id).child("/kota");
//   databaseNam.remove();
//   databaseNam1.remove();
//   databaseNam2.remove();
//   databaseNama.set("hadir");
//   databaseNama1.set("hadir");
//   databaseNama2.set("hadir");
//   res.send("done");
//   // databaseKota.set(kota);

// });

// app.get("/getabsen", function(req, res) {
//   var id = req.query.id;
//   var jurusan = req.query.jurusan;
//   const params = req.url.split("/");
//   const eventId = params[2];
//   return admin.database().ref("absen/" +jurusan+"/"+ id).once("value", (snapshot) => {
//     var event = snapshot.val();
//     if (event){
//       return admin.database().ref("absen/nama/"+jurusan+"/"+ id).once("value", (snapshot) => {
//         var event1 = snapshot.val();
//         if (event1){
//           res.send(event1 + " Telah Hadir");
//         }        
//       });
//     }else{
      
//       return admin.database().ref("absen/nama/"+jurusan+"/"+ id).once("value", (snapshot) => {
//         var event1 = snapshot.val();
//         if (event1){
//           res.send(event1 + " Belum Hadir");
//         }else{
//           res.send("id atau jurusan yang dimasukan salah");
//         }        
//       });
//     }
    
//   });
// });



// app.get("/database", function(req, res) {
//   var id = req.query.id;
//   const params = req.url.split("/");
//   const eventId = params[2];
//   return admin.database().ref("users/" + id).once("value", (snapshot) => {
//     var event = snapshot.val();
//     res.send(`
//       <!doctype html>
//       <html>
//         <head>
//           <title>${id}</title>
//         </head>
//         <body>
//           <h1> ${event.nama} rumahnya ${event.kota}</h1>
//         </body>
//       </html>`);
//   });
// });

exports.project = functions.https.onRequest(app);

exports.login = functions.auth.user().onCreate((user) => { // ...
  const emailLogin = user.email;
  const uriLogin = user.photoURL;
  const uidLogin = user.uid; // The email of the user.
  const databaseEmailLogin = admin.database().ref("users/" + uidLogin + "/email");
  const databaseUriLogin = admin.database().ref("users/" + uidLogin + "/photoUrl");
  // res.send("done");
  databaseUriLogin.set(uriLogin);
  databaseEmailLogin.set(emailLogin);

});


exports.onDeleted = functions.auth.user().onDelete((user) => {
  const uidDeleted = user.uid; // The email of the user.
  const databaseEmailDeleted = admin.database().ref("users/" + uidDeleted);
  databaseEmailDeleted.remove();
});
// // Create and deploy your first functions
// // https://firebase.google.com/docs/functions/get-started
//
exports.main = functions.https.onRequest((request, response) => {
  functions.logger.info("Hello logs!", {structuredData: true});
  response.send("Hello from Firebase!");
});
