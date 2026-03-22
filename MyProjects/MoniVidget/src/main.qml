import QtQuick
import QtQuick.Window
import QtQuick.Controls

Window {
    x: Screen.width - 250
    y: Screen.height - 280
    id: window
    width: 250
    height: 280
    visible: true
    title: qsTr("Just Monika")
    flags: Qt.FramelessWindowHint
    color: "transparent"
    
    FontLoader {
        id: font
        source: "../fonts/Oswald.ttf"
    }
    
    Image {
        opacity: opacitySlider.value
        width: 250
        height: 250
        source: "../images/Moni.svg"
        
    }
    
    Rectangle {
        opacity: opacitySlider.value
        x: 0
        y: 250
        width: 220
        height: 30
        color: "transparent"
        
        Image {
            anchors.fill: parent
            source: "../images/text.png"
        }
        
        Text {
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            font.family: font.name
            property int clicks: 0
            id: click_count
            objectName: "click_count"
            anchors.fill: parent
            text: click_count.clicks
            font.pointSize: 14
            color: "#000000"
        }
    }

    Rectangle {
        opacity: opacitySlider.value
        x: 220
        y: 250
        width: 30
        height: 30
        color: "transparent"

        Image {
            anchors.fill: parent
            source: "../images/menu_button.png"
        }

        MouseArea {
            anchors.fill: parent
            onClicked: { menu.visible = !menu.visible }
        }
    }

    Rectangle {
        width: 175
        height: 200
        x: 65
        y: 20
        color: "transparent"
        id: menu
        visible: false
        
        Image {
            anchors.fill: parent
            source: "../images/menu.png"
        }

        Rectangle {
            x: 10
            y: 10
            width: 150
            height: 30
            color: "transparent"
            
            Image {
                anchors.fill: parent
                source: "../images/opacity.png"
            }

            Slider {
                x: 50
                y: 5
                width: 90
                height: 20
                id: opacitySlider
                value: 1
                from: 0.05
                to: 1.0
            }
        }

        Rectangle {
            x: 10
            y: 60
            width: 150
            height: 30
            color: "transparent"
            
            Rectangle {
                z: 3
                anchors.fill: parent
                color: "black"
                opacity: 0
                MouseArea {
                    anchors.fill: parent
                    hoverEnabled: true
                    onClicked: { window.flags = window.flags ^ Qt.WindowStaysOnTopHint }
                    onEntered: { parent.opacity = 0.15}
                    onExited: {parent.opacity = 0.0}
                }
            }

            Image {
                anchors.fill: parent
                source: "../images/pin.png"
            }

            Text {
                width: parent.width - 20
                height: parent. height
                x: 30
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                font.family: font.name
                text: "Pin window"
                font.pointSize: 14
                color: "#000000"
            }
        }

        Rectangle {
            x: 10
            y: 110
            width: 150
            height: 30
            color: "transparent"
            
            Rectangle {
                z: 3
                anchors.fill: parent
                color: "black"
                opacity: 0
                MouseArea {
                    anchors.fill: parent
                    hoverEnabled: true
                    onClicked: {  }
                    onEntered: { parent.opacity = 0.15}
                    onExited: {parent.opacity = 0.0}
                }
            }

            Image {
                anchors.fill: parent
                source: "../images/character.png"
            }

            Text {
                width: parent.width - 20
                height: parent. height
                x: 30
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                font.family: font.name
                text: "Change character"
                font.pointSize: 12
                color: "#000000"
            }
        }

        Rectangle {
            x: 10
            y: 160
            width: 150
            height: 30
            color: "transparent"
            
            Rectangle {
                z: 3
                anchors.fill: parent
                color: "black"
                opacity: 0
                MouseArea {
                    anchors.fill: parent
                    hoverEnabled: true
                    onClicked: backend.app_exit()
                    onEntered: { parent.opacity = 0.15}
                    onExited: {parent.opacity = 0.0}
                }
            }

            Image {
                anchors.fill: parent
                source: "../images/close.png"
            }

            Text {
                width: parent.width - 20
                height: parent. height
                x: 30
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                font.family: font.name
                text: "Close app"
                font.pointSize: 12
                color: "#000000"
            }

            
        }
    }
}