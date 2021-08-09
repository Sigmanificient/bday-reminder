document.getElementById('birthday_form').addEventListener(
    'submit', async (e) => {
        e.preventDefault()

        let searchUser = e.target.parentNode.querySelector('#search').value

        if (searchUser !== '') {
            let url = `${window.location}api/search/${searchUser}`

            await fetch(url)
                .then((r) => r.json())
                .then((json) => console.log(json))
        }
    }
)
