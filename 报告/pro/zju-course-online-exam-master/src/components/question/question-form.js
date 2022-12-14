import React, { Component } from 'react'
import {Form, Select, AutoComplete, Button, Input, List, Icon} from 'antd'
import {formItemLayoutWithLabel, formItemLayoutWithoutLabel} from '../../form'

const Option = Select.Option
const AutoCompleteOption = AutoComplete.Option
const TextArea = Input.TextArea

const option_index = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S']

let uuid = 0
class RawForm extends Component {
  constructor(props){
    super(props)
    // this.state = props.question
  }

  remove = (option) => {
    const { form } = this.props;
    // can use data-binding to get
    const optionId = form.getFieldValue('optionId');
    // We need at least one option
    if (optionId.length === 0) {
      return;
    }

    // can use data-binding to set
    form.setFieldsValue({
      optionId: optionId.filter(key => key !== option),
    });
  }

  add = () => {
    const { form } = this.props;
    // can use data-binding to get
    const optionId = form.getFieldValue('optionId');
    const nextOption = optionId.concat(uuid);
    // console.log(nextOption)
    uuid++;
    // can use data-binding to set
    // important! notify form to detect changes
    form.setFieldsValue({
      optionId: nextOption,
    });
  }

  handleSubmit = (e) => {
    e.preventDefault();
    this.props.form.validateFields((err, values) => {
      if (!err) {
        console.log(values)
        const data={
          type:values.type,
          description:values.description,
          keypoints:values.keypoints,
          options:values.optionId.map((id,index)=>{
            return {key:option_index[index],content:values.optionContent[id]}
          }),
          solution:option_index[values.optionId.indexOf(values.correctOptionId)]
        }
        let onSubmit = this.props.onSubmit
        if(onSubmit){
          console.log(data)
          onSubmit(data)
        }
      }
    });
  }


  render(){
    const { getFieldDecorator,getFieldValue } = this.props.form;
    getFieldDecorator('optionId', { initialValue: [] });
    const optionId = getFieldValue('optionId');
    const formItems = optionId.map((option, index) => {
      return (
        <Form.Item
          {...formItemLayoutWithLabel}
          label={'??????'+option_index[index]}
          required={false}
          key={option}
        >
          {getFieldDecorator(`optionContent[${option}]`, {
            validateTrigger: ['onChange', 'onBlur'],
            rules: [{
              required: true,
              whitespace: true,
              message: "?????????????????????",
            }],
          })(
            <Input placeholder="????????????" style={{ width: '60%', marginRight: 8 }} />
          )}
          {optionId.length > 0 ? (
            <Icon
              className="dynamic-delete-button"
              type="minus-circle-o"
              disabled={optionId.length === 0}
              onClick={() => this.remove(option)}
            />
          ) : null}
        </Form.Item>
      )
    })
    // const option_index_list=null
    // console.log(optionId)
    const option_index_list=optionId.map((option,index)=>{
      return(
        <Option key={option} value={option}>{option_index[index]}</Option>
      )
    })
    return (
      <Form onSubmit={this.handleSubmit}>
        <Form.Item {...formItemLayoutWithLabel} label='????????????'>
          {getFieldDecorator('description',{})(
            <Input/>
          )}
        </Form.Item>
        <Form.Item {...formItemLayoutWithLabel} label={'??????'}>
          {getFieldDecorator('type')(
            <Select >
              <Option value={'?????????'}>?????????</Option>
              <Option value={'?????????'}>?????????</Option>
            </Select>
          )}
        </Form.Item>
        <Form.Item {...formItemLayoutWithLabel} label={'??????????????????'}>
          {getFieldDecorator('keypoints',{})(
            <Input/>
          )}
        </Form.Item>
        {formItems}
        <Form.Item {...formItemLayoutWithoutLabel}>
          <Button type="dashed" onClick={this.add} style={{ width: '60%' }}>
            <Icon type="plus" /> ????????????
          </Button>
        </Form.Item>
        <Form.Item {...formItemLayoutWithLabel} label={'????????????'}>
          {getFieldDecorator('correctOptionId')(
            <Select>
              {option_index_list}
            </Select>
          )}
        </Form.Item>
        <Form.Item {...formItemLayoutWithoutLabel}>
          <Button type="primary" htmlType="submit">??????</Button>
        </Form.Item>
      </Form>
    )
  }
}


export const QuestionForm = Form.create({
  mapPropsToFields(props) {
    // console.log(props)
    const question = props.question
    console.log(question)
    let fieldObj={}
    if(question!=null){
    fieldObj.keypoints= Form.createFormField({
      value:question.keypoints
    })
    fieldObj.description = Form.createFormField({
      value:question.description
    })
    fieldObj.type = Form.createFormField({
      value:question.type
    })
    fieldObj.optionContent =question.options.map((option,index)=>{
      return Form.createFormField({
        value:option.content
      })
    })
      
    fieldObj.optionId=Form.createFormField({
      value:question.options.map((option,index)=>{
        return index
      })
    })
    fieldObj.correctOptionId = Form.createFormField({
      value:option_index.indexOf(question.solution)
    })
      console.log(fieldObj)
    // for(let key of Object.keys(props.question)){
    //   fieldObj[key] = Form.createFormField({
    //     value: props.question[key],
    //   })
    // }

    }
    return fieldObj
  },
})(RawForm)
