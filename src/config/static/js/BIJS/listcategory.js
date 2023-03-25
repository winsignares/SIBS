function listcategory(){
    axios.get('/viewlistcategory',{
        responseType: 'json'
    })
    .then(function(res){
        console.log(res);
    })
    .catch(function(err){
        console.log(err);
    })
    .then(function(){
    });
}

/*  axios.get('/viewlistcategory',{
        .then(function(response){
            console.log(response);
        }).catch(function(error){
            console.log(error);
    })
        .then(function(){
    })
    })

axios.get('/viewlistcategory').then((response)=>{
    setPost(response.data);
}
)*/
