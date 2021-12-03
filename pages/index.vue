<template>
<body class="h-screen overflow-hidden flex items-center justify-center">
  <SearchBar/>
</body>
</template>

<script>
export default {

   methods : {
     getAllFromDB () {

       let sauveteurs;
       let bateaux;

       var config = {method: 'get', url: 'https://api.ndi.haysberg.io/sauveteurs'};
       axios(config)
         .then(function (response) {
           sauveteurs = response;
           console.log(JSON.stringify(response.data));
         })
         .catch(function (error) {
           console.log(error);
         });


       var config = {method: 'get', url: 'https://api.ndi.haysberg.io/bateaux'};
       axios(config)
         .then(function (response) {
           bateaux = response;
           console.log(JSON.stringify(response.data));
         })
         .catch(function (error) {
           console.log(error);
         });


       let gigaListe = Object.assign(bateaux, sauveteurs)
     }
  },

}
</script>
