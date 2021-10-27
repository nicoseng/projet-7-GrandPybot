/* Je déclare ma variable avec le mot-clé let puis je sélectionne la balise HTML qui m'intéresse */

/* Avec la méthode .textContent, j'introduis le texte que je souhaite */

$(document).ready(function(){

        $('.loading_place').css("visibility","hidden");
        $(".result").css("visibility","hidden");

        let initMap = function initMap(lat,lng){

               let place = {
                       lat:lat,
                       lng:lng
               };



               let map = new google.maps.Map(document.getElementById('map'),{
                       center: place,
                       zoom: 8,
               });

               let infos = new google.maps.InfoWindow({
                       content:content
               });

               let marker = new google.maps.Marker({
                       position : place,
                       map: map
               });

               marker.addListener('click', function(){
                   infos.open(map, marker);
               });
       };

        $("#send").click(function(e){ //e = event click propagé par ton click sur envoyer
 		e.preventDefault(); // on coupe le comportement par défaut
 		$('.loading_place').css("visibility","visible");

                // Je récupère la valeur du champ dont l'id est "question" dans la page index.html pour mettre cette valeur dans la console et pouvoir la traiter
 		let questionContent = $("#question").val();
 		
                // J'affiche le contenu de mon champ contenant la question pour vérifier si tout va bien 
                console.log(questionContent);
 		
                let result = $("#result");

                $(".dialog_box").append(questionContent + "<br/>" );



                //J'envoie les données récupérées dans la console avec une requête de type POST via la techno AJAX vers mon serveur flask pour qu'il traite ma demande
                $.post(

                        "/api", // Je cherche la route que je veux cibler (Vérifier que je l'ai créée coté serveur Flask, sinon créer la route en question)

                        {
                        
                        // Je récupère la valeur des inputs qu'on va faire passer dans la route nommée /api avec une variable question que je définis (je choisis le nom de variable que je veux)
                        question: questionContent

                        },

                // Une fois que c'est "fait" (d'où le .done()), je définis une fonction que j'appelle response et dans laquelle j'affiche le résultat avec une variable response que je définis et j'affiche dans la console le résultat renvoyé en Flask par return jsonify (l.28)
                ).done(function (response) {

                        console.log(response);
                        
                // Je décide d'afficher le résultat coté client via HTML

                        $(".papybot_response").html(response["papybot_response"]);
                        $(".address").html(response["address"]);
                        $(".latitude").html(response["latitude"]);
                        $(".longitude").html(response["longitude"]);
                        $(".extract").html(response["extract"]);


                        let lat = parseFloat(response["latitude"]);
                        let lng = parseFloat(response["longitude"]);
                        let address = response["address"];

                        //let papybotQuote = papybot_quote;
                        //$(".papybot_response").append(papybotQuote);

                        $(".loading_place").remove();
                        $(".result").css("visibility","visible");
                        initMap(lat,lng);

                });
        });
});