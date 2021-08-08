window.onload = () => {
    const SearchBirthdayForm = document.getElementById('birthday_form')
    SearchBirthdayForm.addEventListener('submit', HandleSearchBirthdayForm)
}

async function HandleSearchBirthdayForm(e) {
    e.preventDefault()

    let searchUser = document.getElementById('search').value
    let url = `${window.location}api/search/${searchUser}`

    await fetch(url).then(
        (r) => {
            return r.json();
        }
    ).then(
        (json) => {
            console.log(json);
        }
    )
}
