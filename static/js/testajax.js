function like(slug,id){
    var element = document.getElementById("like")
    var count = document.getElementById("count")
    $.get(`/like/${slug}/${id}`).then(response =>{
        if(response['response'] ==="liked"){
            element.className = "fa fa-heart"
            element.innerText = Number(element.innerText + 1)
        }else{
            element.className = "fa fa-heart-o"
             element.innerText = Number(element.innerText - 1)
        }
    })
}