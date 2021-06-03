class Header extends HTMLElement {
    constructor() {
      super();
    }

    connectedCallback() {
        this.innerHTML = `
        <style>
        .header {
            background-color: #88BACF;
            height: 70px;
            line-height: 70px;
        }
        
        

        .logo img{
            
            float: left;
            
            background-repeat: no-repeat;
            background-size: cover;
            padding: 5px 0px 5px 0px;
            margin: 0px;
            width: 130px;
            height: 70px;
        }
        
        .menu {
            float: right;
        }
        
        .menu a {
            color: #ffffff;
            margin-right: 20px;
        }
        
        .menu a:hover {
            color: #547280;
        }
        
        .container-fluid {
            padding: 0;
        }

        .menu input[type=text] {
            float: right;
            padding: 6px;
            border: none;
            margin-top: 24px;
            margin-right: 14px;
            font-size: 17px;
            height: 30px;
            line-height: 50px;
          }
          

        </style>
        <header class="container-fluid header" id="myHeader">
            <div class="container">
                <a href='/' class="logo"><img src="static/img/logo_tn.png" alt="logo"/></a>
                <nav class="menu">
                    <a href='charts'>Statistiques</a>
                    <a href='/parcours'>Parcours des données</a>
                    <a href='#about'>TIPE</a>
                    <a href='ListeEcoleRequete'>Liste Ecoles Requete</a>
                    <a href='recherche'>Requetes_SQL</a>
                    <a href='#contact'>Contact</a>
                    <input type="text" placeholder="Recherche par Identifiant.." size=12>
                </nav>
            </div>
        </header>
      `;

    }
}

customElements.define('header-component', Header);
  