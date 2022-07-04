function appendChat(user, bot){
    console.log('Trying to append')
    console.log(user, bot)
    $('#botbox').append(`<div class="dialogbox user">${user}</div>
                         <div class="dialogbox bot">${bot}</div>`);

    const $element = document.getElementById('botbox');
    $element.scrollTop = $element.scrollHeight;
}

document.getElementById('chatForm').addEventListener('submit', function(e){
        e.preventDefault();
        userInputTag = document.getElementById('user_query');
        user_input = userInputTag.value;
        if(user_input == '안녕'){
          bot_output = '만나서 반가워요.'
        }else if(user_input == '잘가'){
          bot_output = '함께 이야기할 수 있어서 즐거웠어요. 언제든 또 오세요 :-)'
        }else{
          bot_output = '죄송합니다. 잘 모르겠어요 :('
        }

        // fetch('../chat', {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json',
        //     },
        //     body: JSON.stringify({name: user_input}),
        // }).then(response => response.json()).then(some => appendChat(user_input, some))
        // userInputTag.value = "";

        appendChat(user_input, bot_output)
        userInputTag.value = "";
    });
