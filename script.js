*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:Segoe UI, sans-serif;
}

body{
background:#f4f6f9;
}

/* NAVBAR */

.navbar{

position:absolute;
top:0;
width:100%;
display:flex;
justify-content:space-between;
align-items:center;
padding:20px 60px;
color:white;
z-index:10;

}

.logo{

font-size:22px;
font-weight:bold;

}

nav a{

color:white;
text-decoration:none;
margin-left:30px;
font-size:15px;

}

nav a:hover{

text-decoration:underline;

}

/* HERO */

.hero{

height:100vh;

background-image:linear-gradient(
rgba(0,0,0,0.6),
rgba(0,0,0,0.6)
),

url("https://images.unsplash.com/photo-1519389950473-47ba0277781c");

background-size:cover;
background-position:center;

display:flex;
justify-content:center;
align-items:center;
text-align:center;
color:white;

}

/* contenido */

.hero-content{

max-width:700px;

}

.hero h1{

font-size:50px;
margin-bottom:20px;

}

.hero p{

font-size:20px;
margin-bottom:30px;
opacity:0.9;

}

/* botón principal */

.btn-principal{

display:inline-block;
padding:14px 35px;
background:#2a5bd7;
color:white;
text-decoration:none;
border-radius:6px;
font-size:16px;
transition:0.3s;

}

.btn-principal:hover{

background:#1e43a3;
transform:scale(1.05);

}
.botones{

display:flex;
justify-content:center;
gap:20px;

}

/* boton registrar */

.btn-secundario{

display:inline-block;
padding:14px 20px;
background:white;
color:#2a5bd7;
text-decoration:none;
border-radius:6px;
font-size:16px;
border:2px solid white;
transition:0.3s;

}

.btn-secundario:hover{

background:#e8ecff;
transform:scale(1.05);

}

form{

display:flex;
flex-direction:column;
gap:15px;
margin-top:20px;

}

input{

padding:12px;
border:none;
border-radius:6px;
font-size:15px;

}

.resultado{

background:white;
padding:10px;
border-radius:8px;
color:black;
margin-top:20px;

}