import  Axios from 'axios';
function listcategory(){
  Axios.get('/viewlistcategory').then((response) => {
    setPost(response.result_Categoria)
    console.log(response)
  })
}



/*  axios.get('/viewlistcategory',{
        .then(function(response){
            console.log(response)
        }).catch(function(error){
            console.log(error)
    })
        .then(function(){
    })
    })

axios.get('/viewlistcategory').then((response)=>{
    setPost(response.data)
}
)*/