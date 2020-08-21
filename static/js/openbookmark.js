// form 
let frm = document.forms["frm"];

// 버튼들 
let addBtn = document.getElementById("submit-btn");
let resetBtn = document.getElementById("reset-btn");

// 북마크 리스트 
let bookmarkList = document.getElementById("bookmark-list");

// form reset 
function reset() {
    frm.elements.namedItem("id").value = ''
    frm.elements.namedItem("title").value = '';
    frm.elements.namedItem("url").value = '';
}

// 취소 버튼 핸들러 등록 
resetBtn.addEventListener("click", reset);

// DOM에 새로운 bookmark 정보 추가 
function addItem(bookmark) { 
    let templ = ` <a href="${bookmark.url}" class="bookmark-link">${bookmark.title}</a> 
    [<a href="#" class="edit-btn">수정</a>] 
    [<a href="#" class="delete-btn">삭제</a>] 
    `; 
    let el = document.createElement('li'); 
    el.dataset.itemId = bookmark.id; 
    el.classList.add("list-item"); 
    el.innerHTML = templ; bookmarkList.appendChild(el); 
} 

// 초기 목록 얻기 
axios.get("http://127.0.0.1:8000/api/bookmark") 
.then(res=>{ 
    console.log(res);
    res.data.datas.forEach(item=>addItem(item)); 
}).catch(e=>console.log(e));