var hand_raise = 1
// type 1 = hand raised
// type 2 = raise accepted
// type 3 = host role change to handler
// type 4 = host role change to cohost
var loc = window.location
var wsStart = 'ws://'
var endPoint = wsStart+loc.host+loc.pathname;
var websocket1
websocket1 = new WebSocket(endPoint)
// console.log(websocket1.url)
const user1 = JSON.parse(document.getElementById('json-username').textContent);
console.log(user1)
var role = localStorage.getItem('role')
console.log(role)
var raise = document.getElementById('raise')
if (role === 'host'){
    raise.style.display='none'
}
websocket1.addEventListener('open',async (e) => {
    raise.addEventListener('click',() =>{
        var result = JSON.stringify({
            'name':user1,
            'data':hand_raise,

        })
        websocket1.send(result)
        

    })

})
var id
abc = []
websocket1.addEventListener('message',async (e) => {
    
    var recieved = JSON.parse(e.data)
    var user = recieved.name
    
    var type = recieved.data
    // console.log(type,user)
    if(type == 'connected'){
        user.forEach(function (item, index) {
            if(abc.includes(item) === false){
                abc.push(item)
                console.log(abc)
            }
            
            
          })
          abc.forEach(function(item){
            if(user1 !== item){
                var list = document.createElement('li')
                var name = document.createElement('p')
                var id1 = document.createElement('div')
                var roles = document.createElement('div')
                var handler = document.createElement('div')
                var cohost = document.createElement('div')
                var audience = document.createElement('div')
                handler.setAttribute('data-tooltip', 'Handler');
                handler.id = 'userhandler -'+item
                cohost.setAttribute('data-tooltip', 'CoHost');
                cohost.id = 'usercohost -'+item
                audience.setAttribute('data-tooltip', 'Audience');
                audience.id = 'useraudience -'+item
                handler.innerHTML = `<i class="fa-solid fa-handshake" aria-hidden="true"></i>
                <span id="people" class="people" name="people">Handler</span>`
                cohost.innerHTML = `<i class="fa-solid fa-hand-fist" aria-hidden="true"></i>
                <span id="people" class="people" name="people">Cohost</span>`
                audience.innerHTML= `<i class="fa-solid fa-users-viewfinder" aria-hidden="true"></i>
                <span id="people" class="people" name="people">Audience</span>`
                roles.className ='roles'
                id1.className='id1'
                roles.appendChild(handler)
                roles.appendChild(cohost)
                roles.appendChild(audience)
                var image = document.createElement('img')
                image.style.cssText="width:68px ;position:relative;left: 13px;right: -10px;padding: 10px;"
                image.src="https://png.pngtree.com/png-vector/20220817/ourmid/pngtree-cartoon-man-avatar-vector-ilustration-png-image_6111064.png"
                id1.appendChild(image)
                id1.appendChild(roles)
                name.innerHTML = item
                list.appendChild(id1)
                list.appendChild(name)
                document.getElementById('list').appendChild(list)
                // var button = document.createElement('BUTTON')
                // var text = document.createTextNode("handler");
                // button.id = 'userhandler -'+item
                // button.appendChild(text)
                // document.getElementById('users').appendChild(button)
                // var button1 = document.createElement('BUTTON')
                // var text1 = document.createTextNode("cohost");
                // button1.id = 'usercohost -'+item
                // button1.appendChild(text1)
                // document.getElementById('users').appendChild(button1)
            } 
          })

        
    }
   
    if (role ==='host' || role ==="handler"){   
        if(type === 1){
            if (confirm('Are you sure you want to save this thing into the database?')) {
                var result = JSON.stringify({
                    'name':user,
                    'data':2,
        
                })
                // Save it!
                websocket1.send(result)
              } else {
                // Do nothing!
                console.log('Thing was not saved to the database.');
              }
        }
    }
    
    if(type===2){
        
        if(user === user1){
            localStorage.setItem('role','cohost')
            role = 'cohost'
            // console.log(role)
        }
    }

    if(type===3){
        
        if(user === user1){
            console.log(type,user)
            localStorage.setItem('role','handler')
            role = 'handler'
            
            console.log(role)
        }
    }
    if(type===4){
        
        if(user === user1){
            console.log(type,user)
            localStorage.setItem('role','cohost')
            role = 'cohost'
            
            console.log(role)
        }
    }
    
    if(role === 'host' || role === 'handler' || role === 'cohost'){
        // console.log('cohost changed')
        hello(role)
    }
    if (typeof abc !== undefined && abc.length>0){
    // var ids=[];
        $('[id^="userhandler -"]').click((e)=>{
            $('[id^="userhandler -"]').each(function(){
                var id=$(this).attr('id');
                sid = id.split("-").pop()
                // console.log(sid);
                var result = JSON.stringify({
                    'name':sid,
                    'data':3,
        
                })
                websocket1.send(result)
            });
        } )
        $('[id^="usercohost -"]').click ((e) => {
            $('[id^="usercohost -"]').each(function(){
                var id=$(this).attr('id');
                sid = id.split("-").pop()
                // console.log(sid);
                var result = JSON.stringify({
                    'name':sid,
                    'data':4,
        
                })
                websocket1.send(result)
            });
        })
    }
})



