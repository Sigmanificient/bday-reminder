window.onload = () => {
    const searchBirthdayForm = document.getElementById('birthday_form')
    searchBirthdayForm.addEventListener(
        'submit', async (e) => {
            e.preventDefault()

            let searchUser = document.getElementById('search').value
            let url = `${window.location}api/search/${searchUser}`

            await fetch(url)
                .then((r) => r.json())
                .then((json) => console.log(json))
        }
    )
}
