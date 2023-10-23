const likeButtons = document.querySelectorAll('.like-button');

likeButtons.forEach(likeButton => {
    likeButton.addEventListener('click', (e) => {
        let likeButtonId = e.currentTarget.id.slice("like-button-".length);
        let likeCounter = document.querySelector(`#like-counter-${likeButtonId}`)

        fetch(`/like-post/${likeButtonId}`, {method: "POST"})
        .then((res) => res.json())
        .then((data) => {
            likeCounter.innerHTML = `(${data['likes']})`
            if (data['liked'] === true) {
                likeButton.classList.add('like-button-liked')
            } else {
                likeButton.classList.remove('like-button-liked')
            }
        }).catch((e) => alert('Could not like post'))
    })
})