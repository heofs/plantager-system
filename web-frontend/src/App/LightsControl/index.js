import React, { useState } from 'react';
import { Slider, Button, Modal, Row, Col } from 'antd';
const marks = {};

for (let x = 0; x <= 24; x++) {
  marks[x] = `${x}h`;
}

export const LightsControl = () => {
  const default_lights = [6, 21];
  const [lights, setLights] = useState(default_lights);
  const [modalText, setModalText] = useState('Content of the modal');
  const [modalVisible, setModalVisible] = useState(false);
  const [confirmLoading, setConfirmLoading] = useState(false);

  const handleSave = () => {
    console.log(lights);
    setModalVisible(true);
  };

  const handleOk = () => {
    setModalText('The modal will be closed after two seconds');
    setConfirmLoading(true);

    setTimeout(() => {
      setConfirmLoading(false);
      setModalVisible(false);
    }, 2000);
  };

  const handleCancel = () => {
    console.log('Clicked cancel button');
    setModalVisible(false);
  };

  return (
    <Row>
      <Col span={24}>
        <h2 style={{ textAlign: 'center' }}>Set lights cycle</h2>
      </Col>
      <Col span={24}>
        <Slider
          range
          marks={marks}
          defaultValue={default_lights}
          max={24}
          dots={true}
          onChange={(range) => setLights(range)}
        />
      </Col>
      <Col span={24}>
        <Button type="primary" block onClick={handleSave}>
          Save
        </Button>
      </Col>
      <Modal
        title="Title"
        visible={modalVisible}
        onOk={handleOk}
        confirmLoading={confirmLoading}
        onCancel={handleCancel}
      >
        <p>{modalText}</p>
      </Modal>
    </Row>
  );
};

export default LightsControl;
