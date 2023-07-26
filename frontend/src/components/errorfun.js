
let errors_check = {subject : '',content : ''}
let valid = {subject : false, content : false}

const subject_Error = (subject) => {

    valid.subject = false
    errors_check.subject = ''

    if (subject.trim().length < 5) {
        valid.subject = true
        errors_check.subject = '제목은 최소 5글자 이상이여야 합니다.'
    }
};

const content_Error = (content) => {

    valid.content = false
    errors_check.content = ''

    if (content.trim().length < 1) {
        valid.content = true
        errors_check.content = '내용을 작성해주세요.'
    }
};

export const Error_sc = (subject, content) => {
    subject_Error(subject)
    content_Error(content)

    return {valid, errors_check}
}

export const Error_c = (content) => {
    content_Error(content)

    return {valid, errors_check}
}

export default Error_sc;
